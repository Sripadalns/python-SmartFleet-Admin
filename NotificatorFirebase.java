/*
 * Copyright 2018 Anton Tananaev (anton@traccar.org)
 * Copyright 2018 Andrey Kunitsyn (andrey@traccar.org)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.traccar.notificators;

import com.fasterxml.jackson.annotation.JsonProperty;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.traccar.Context;
import org.traccar.model.Event;
import org.traccar.model.Position;
import org.traccar.model.User;
import org.traccar.notification.NotificationFormatter;

import javax.ws.rs.client.Entity;
import javax.ws.rs.client.InvocationCallback;

public class NotificatorFirebase extends Notificator {

    private static final Logger LOGGER = LoggerFactory.getLogger(NotificatorFirebase.class);

    private static final String URL = "https://fcm.googleapis.com/fcm/send";

    private String key;

    public static class Notification {
        @JsonProperty("body")
        private String body;
        @JsonProperty("sound")
        private String sound;
    }
    public static class Data {
        @JsonProperty("body")
        private String body;
        @JsonProperty("sound")
        private String sound;
    }
    public static class Message {
        @JsonProperty("registration_ids")
        private String[] tokens;
        @JsonProperty("notification")
        private Notification notification;
        @JsonProperty("data")
        private Data data;
    }

    public NotificatorFirebase() {
        key = Context.getConfig().getString("notificator.firebase.key");
    }

    @Override
    public void sendSync(long userId, Event event, Position position) {
        final User user = Context.getPermissionsManager().getUser(userId);
        if (user.getAttributes().containsKey("notificationTokens")) {

            Notification notification = new Notification();
            notification.body = NotificationFormatter.formatShortMessage(userId, event, position).trim();
            notification.sound = "siren";
            Data data = new Data();
            data.body = NotificationFormatter.formatShortMessage(userId, event, position).trim();
            data.sound = "siren";
            Message message = new Message();
            message.tokens = user.getString("notificationTokens").split("[, ]");
            /*message.notification = notification;*/
            message.data = data;
            Context.getClient().target(URL).request()
                    .header("Authorization", "key=" + key)
                    .async().post(Entity.json(message), new InvocationCallback<Object>() {
                @Override
                public void completed(Object o) {
                }

                @Override
                public void failed(Throwable throwable) {
                    LOGGER.warn("Firebase notification error", throwable);
                }
            });
        }
    }

    @Override
    public void sendAsync(long userId, Event event, Position position) {
        sendSync(userId, event, position);
    }

}
