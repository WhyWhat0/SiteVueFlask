<template>
    <div v-if="show" @click="hideDialog">
        <div @click.stop class="chat">
            <div class="chat-header">
                <div class="chat-header-name-date">
                    <div class="chat-header-name">{{ getMessageModeName }}</div>
                    <div class="chat-header-date ">{{ myDate() }}
                    </div>
                </div>
                <div class="chat-header-buttons">
                    <div class="chat-header-button">
                        <i class="fa fa-search" aria-hidden="true"></i>
                    </div>
                    <div class="chat-header-button" @click="changeModeMessange">
                        <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                    </div>
                    <div class="chat-header-button" @click="goToBot">
                        <i class="fa fa-chevron-right" aria-hidden="true"></i>
                    </div>
                </div>
            </div>

            <PostMessages
                ref="chatBody"
                :messagesBot="messagesBot"
                :messagesHuman="messagesHuman">
            </PostMessages>
            <PostCreateForm
                @scrollToBottom="handleScrollToBottom">
            </PostCreateForm>
        </div>
    </div>
</template>
<script>
import PostMessages from "@/components/PostMessages.vue"
import PostCreateForm from "@/components/PostCreateForm.vue"
import postGetApi from "@/mixins/postGetApi"
import { mapState, mapGetters, mapMutations, mapActions } from "vuex"
import axios from "axios"
export default {
    components: { PostMessages, PostCreateForm },
    name: 'post-tg-form',
    mixins: [postGetApi],
    data() {
        return {
        }
    },
    props: {
        show: {
            type: Boolean,
            default: false
        }
    },
    computed: {
        ...mapState({
            messagesBot: state => state.messagesBot,
            messagesHuman: state => state.messagesHuman,
            messangerMode: state => state.messangerMode,
            humanAssistantName: state => state.humanAssistantName
        }),
        ...mapGetters({
            getMessageModeName: 'getMessageModeName'
        }),
    },
    methods: {
        ...mapActions({
            getPostAnswersList: 'getPostAnswersList'
        }),
        ...mapMutations({
        }),

        goToBot() {
            window.open('https://t.me/pancake1953bot')
        },
        changeModeMessange() {
            this.messangerMode.human = !this.messangerMode.human;
            this.messangerMode.bot = !this.messangerMode.bot;
            console.log(this.messangerMode.human, this.messangerMode.bot)
        },
        hideDialog() {
            this.$emit('update:show', false)
        },
        handleScrollToBottom() {
            this.$refs.chatBody.scrollToBottom();
            const chatBody = this.$refs.chatBody;
            chatBody.scrollTop = chatBody.scrollHeight;
        },
        myDate() {
            const today = new Date();
            const yyyy = today.getFullYear();
            let mm = today.getMonth() + 1; // Months start at 0!
            let dd = today.getDate();

            if (dd < 10) dd = '0' + dd;
            if (mm < 10) mm = '0' + mm;

            const formattedToday = dd + '/' + mm + '/' + yyyy;
            return formattedToday
        }

    },
    mounted() {
    }
}
</script>
<style>
.dialog {
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background: rgba(197, 190, 190, 0.5);
    position: fixed;
    display: flex;
}

.smth {
    background: blue;
    height: 10px;
}
</style>