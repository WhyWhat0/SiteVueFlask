<template>
    <div class="chat-footer" :style="{ height: this.chatFooterHeight + '%' }">
        <div class="chat-footer-item">
            <i class="fa fa-paperclip fa-flip-horizontal fa-fw" aria-hidden="true" style="font-size: 25px;"></i>
        </div>
        <div class="chat-footer-text-area grow-wrap" style="margin-left: 10px;">
            <textarea
                v-focus
                id="ta"
                @submit.prevent
                :value="currentMessage"
                @input="updateCurrentMessage"
                class="message-text"
                rows="1"
                style="font-size: 16px; line-height: 20px;  overflow-y: scroll;"
                placeholder="Write a message..."
                type="text"
                @keydown.enter.prevent.exact="createMyMessage"
                @keydown.shift.enter.prevent="newLine">
                </textarea>

        </div>
        <div class="chat-footer-item" style="margin-right: 10px;">
            <div
                style="font-size: 25px;"
                class="fa fa-paper-plane fa-fw"
                aria-hidden="true"
                @click="createMyMessage">
            </div>
        </div>
    </div>
</template>
<script>
import { mapState, mapGetters, mapActions, mapMutations } from 'vuex'
import toggleMixin from "@/mixins/toggleMixin";
import axios from 'axios';
export default {
    name: "post-create-form",
    mixins: [toggleMixin],
    data() {
        return {
            msg: '',
            path: 'http://localhost:5000/bot',
            message: {
                id: '',
                text: '',
                date: '',
                files: '',
                isMyMessage: true,
                handlers: {
                    mouseup: "calculateHeight",
                    keyup: "calculateHeight",
                    onmouseup: "calculateHeight",
                    onkeyup: "calculateHeight",
                }
            },
        }
    },
    mounted() {
        this.changeFooterArea(1);
    },
    methods: {
        ...mapMutations({
            setCurrentMessage: 'setCurrentMessage',
            setSizeFooterArea: 'setSizeFooterArea',
            setMessagesCount: 'setMessagesCount'
        }),

        updateCurrentMessage(e) {
            this.$store.commit('setCurrentMessage', e.target.value)
        },
        async createMyMessage() {
            this.message.id = Date.now();
            this.message.date = this.$store.getters.myTime;
            this.message.text = this.currentMessage;
            this.message.isMyMessage = true
            this.pushMessage(this.message)
            this.$store.commit('setCurrentMessage', '')
            this.changeFooterArea(1)
            this.changeDivArea()
            await axios.post(this.path, this.message)
            this.$store.commit('setMessagesCount', this.messagesCount + 1)
            // const answer = this.getPostMessage((this.messagesBot.length + 1) / 2 - 1)
            this.msg = await this.getPostMessage((this.messagesBot.length + 1) / 2 - 1)
            await this.pushMessage(this.msg)
            this.$emit('scrollToBottom')
            this.message = {
                id: '',
                text: '',
                date: '',
                files: '',
                isMyMessage: '',
            }
        },
        pushMessage(message) {
            if (message.text) {
                if (this.messangerMode.bot) {
                    this.messagesBot.push(message);
                }
                else {
                    this.messagesHuman.push(message);
                }

            }

        },

        async getPostMessage(id = 0) {
            await axios.get(this.path)
                .then((res) => {
                    this.msg = res.data.answersList[id];
                })
                .catch((error) => {
                    // eslint-выключение следующей строки
                    console.error(error);
                });
            console.log(this.msg, 'inside')
            return this.msg
        },
        newLine(e) {
            this.changeFooterArea(this.calculateHeight() + 1)
            setTimeout(() => {
                e.target.value += '\n'
                // let caret = e.target.selectionStart;
                // e.target.setRangeText("\n", caret, caret, "end");
            }, 1);
        },
        changeFooterArea(col) {
            this.$store.commit('setSizeFooterArea', col)
        },
        changeDivArea() {
            ta.rows = this.sizeFooterArea
            if (this.sizeFooterArea < 10) {
                this.$store.commit('setChatBodyHeight', 84 - 3 * (this.sizeFooterArea - 1))
                this.$store.commit('setChatFooterHeight', 8 + 3 * (this.sizeFooterArea - 1))
            }

        }

    },
    computed: {
        ...mapState({
            currentMessage: state => state.currentMessage,
            sizeFooterArea: state => state.sizeFooterArea,
            chatBodyHeight: state => state.chatBodyHeight,
            chatFooterHeight: state => state.chatFooterHeight,
            messagesBot: state => state.messagesBot,
            messagesHuman: state => state.messagesHuman,
            messangerMode: state => state.messangerMode,
            messagesCount: state => state.messagesCount

        })
    },
    watch: {
        currentMessage() {
            this.changeFooterArea(this.calculateHeight())
        },
        sizeFooterArea: {
            handler: function (newValue, oldValue) {
                this.changeDivArea()
            }

        }
    }
}
</script>
<style scoped>
.fa {
    font-size: small;
}

.grow-wrap {
    /* easy way to plop the elements on top of each other and have them both sized based on the tallest one's height */
    display: grid;
}

.grow-wrap::after {
    /* Note the weird space! Needed to preventy jumpy behavior */
    content: attr(data-replicated-value) " ";

    /* This is how textarea text behaves */
    white-space: pre-wrap;

    /* Hidden from view, clicks, and screen readers */
    visibility: hidden;
}

.grow-wrap>textarea {
    /* You could leave this, but after a user resizes, then it ruins the auto sizing */
    resize: none;

    /* Firefox shows scrollbar on growth, you can hide like this. */
    /* overflow: hidden; */
}

.grow-wrap>textarea,
.grow-wrap::after {
    /* Identical styling required!! */
    /* border: 1px solid black; */
    padding: 0.5rem;
    font: inherit;

    /* Place on top of each other */
    grid-area: 1 / 1 / 2 / 2;
}

/* body {
      margin: 2rem;
      font: 1rem/1.4 system-ui, sans-serif;
  } */

label {
    display: block;
}
</style>