<template>
    <!-- :style="{ backgroundImage: 'url(' + require('@/assets/images/images/photo.jpg') + ')', backgroundSize: 'cover' }" -->
    <div class="image">
        <Navbar></Navbar>
        <div v-intersection="showNavbar" class="observer"></div>
        <div class="dialog__content">

        </div>
    </div>
</template>
<script>
import PostTGForm from "@/components/PostTGForm"
import Navbar from "@/components/Navbar"
import axios from "axios"
import postGetApi from "@/mixins/postGetApi"
import { mapActions } from "vuex"
export default {
    components: { PostTGForm, Navbar },
    data() {
        return {
            image: "https://celes.club/uploads/posts/2023-03/1679426930_celes-club-p-fon-vindovs-khp-oboi-7.jpg"
        }
    },
    mixins: [postGetApi],
    methods: {
        ...mapActions({
            getPostAnswersList: 'getPostAnswersList'
        }),
        showNavbar() {
            this.$store.commit('setNavbarVisible', !this.$store.state.navbarVisible)
        },

        async fetchPosts() {
            try {
                setTimeout(async () => {
                    const response = await axios.get('https://jsonplaceholder.typicode.com/posts', {
                        params: {
                            _page: 1,
                            _limit: 10
                        },
                        headers: {
                        }
                    });
                    console.log(response)
                }, 500)

            } catch (e) {
                alert('Ошибка');
            } finally {

            }
        },




    },
    mounted() {
        this.getPostAnswersList()
    }
}
</script>
<style scoped>
.parent-element {
    position: absolute;
    overflow: visible;
    height: 100%;
}

.image {
    background: url('@/assets/images/images/photo.jpg') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    padding: 20px;
}

.dialog__content {
    margin-left: auto;
    margin-right: auto;
    background: lightblue;
    max-width: 70%;
    min-height: 2000px;
    padding: 20px;
    border-radius: 12px;
    /* margin: 0 auto;
	max-width: 970px;
	display: flex;
	background: none;
	border: 0;
	padding: 0 10px; */

}

.fixpos {
    position: fixed;
}

.v-enter-active,
.v-leave-active {
    transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}



.observer {
    height: 5px;
    width: 70%;
    margin: auto;
    /* background: white;
    border: 1px white; */

}
</style>