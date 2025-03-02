import { createStore } from 'vuex'
import { postModule } from './postModule'
import axios from 'axios'
export default createStore({
  state: {
    isAuth: false,
    currentMessage: '',
    dialogVisible: false,
    navbarVisible: true,
    messagesBot: [],
    messagesHuman:[],
    humanAssistantName: 'какой-то чел',
    sizeFooterArea: 1,
    chatBodyHeight: 84,
    chatFooterHeight: 8,
    messagesCount: 0,
    messangerMode: {
      human: false,
      bot: true
  }
  },
  getters: {
    getMessagesBot(state){
      return state.messagesBot
    },
    getMessageModeName(state) {
      if (state.messangerMode.bot) {
          return 'Бот'
      }
      else {
          return state.humanAssistantName
      }
  },
    myTime(state) {
      const today = new Date();
      let hours = today.getHours();
      let minuets = today.getMinutes();
      const formattedToday = hours + ':' + minuets;
      return formattedToday;
    },
    getAuthInfo(state){
      return state.isAuth;
    }

  },
  
  mutations: {
    
    changeModeMessange(state) {
      state.messangerMode.human = !state.messangerMode.human;
      state.messangerMode.bot = !state.messangerMode.bot;
      console.log(state.messangerMode.human, state.messangerMode.bot)
    },
    setMessagesBot(state, list){
      state.messagesBot = list
    },
    setChatFooterHeight(state, size){
      state.chatFooterHeight = size
    },
    setMessagesCount(state, count){
      state.messagesCount = count
    },
    setChatBodyHeight(state, size){
      state.chatBodyHeight = size
    },
    setSizeFooterArea(state, size){
      state.sizeFooterArea = size
    },
    setCurrentMessage(state, message){
      state.currentMessage = message;
    },
    setDialogVisible(state, a){
      state.dialogVisible = a;
    },
    setNavbarVisible(state, a){
      state.navbarVisible = a;
    },
  },
  actions: {
    async getPostAnswersList({commit, state}) {
      await axios.get('http://localhost:5000/bot')
          .then(async (response) => {
            //myList = [...response.data.answersList, ...response.data.messagesList];
              commit('setMessagesBot', response.data.answersList.concat(response.data.messagesList).sort((a, b) => a.id - b.id))
          })
          .catch((error) => {
              // eslint-выключение следующей строки
              console.error(error);
          });
    }
  },
  modules: {
    post: postModule
  }
})
