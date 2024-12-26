<template>
    <div :class="{
        'message-mine': message.isMyMessage,
        'message-bot': !message.isMyMessage
    }">
        <div class="message-body" id="block">
            <div
                class="message-body-text textformat large-font">
                <p style="line-height:1.2em">{{ message.text }}</p>
            </div>
            <div class="message-body-date-seen">
                <div class="message-body-date">{{ message.date }}</div>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    name: 'my-message',
    data() {
        return {

        }
    },
    props: {
        message: {
            type: Object,
        }
    }
}
</script>
<style></style>