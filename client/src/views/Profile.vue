<template>
    <div class="profile-page">
        <section class="section-profile-cover section-shaped my-0">
            <div class="shape shape-style-1 shape-primary shape-skew alpha-4">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </section>
        <section class="section section-skew">
            <div class="container">
                <card shadow class="card-profile mt--300" no-body>
                    <div class="px-4">
                        <div class="row justify-content-center">
                            <div class="col-lg-3 order-lg-2"></div>
                            <div class="col-lg-4 order-lg-3 text-lg-right align-self-lg-center">
                                <div class="card-profile-actions py-4 mt-lg-0">
                                    <base-button @click="logOut" size="sm" class="danger float-right">Log Out</base-button>
                                    <base-button @click="editModal = true" size="sm" class="float-right">Edit Profile</base-button>
                                       <edit-user-modal 
                                        :userInfo="user"
                                        :showSync="editModal" 
                                        @close="editModal = false"
                                        @save="editUser($event)"
                                       >
                                        </edit-user-modal>
                                </div>
                            </div>
                            <div class="col-lg-4 order-lg-1">
                                <div class="card-profile-stats d-flex justify-content-center">
                                </div>
                            </div>
                        </div>
                        <div class="text-center mt-5">
                            <h3>{{ user.username }}
                            </h3>
                            <span class="font-weight-light">{{ safeAge(user.birthdate) }} </span>
                            <span class="font-weight-light">- {{ user.gender }} </span>
                        </div>
                        <div class="mt-5 py-5 border-top text-center">
                            <div class="row justify-content-center">
                                <div class="col-lg-9">
                                    <h4>
                                        Favorite Workouts
                                    </h4>
                                        <accordion 
                                            v-for="(workout, index) in favorites" :key=index 
                                            :obj="workout"
                                            :index="index"
                                        >
                                        </accordion>
                                </div>
                            </div>
                        </div>
                    </div>
                </card>
            </div>
        </section>
    </div>
</template>
<script>

import EditUserModal from './components/EditUserModal'
import Accordion from './components/Accordion'
export default {
    components: {
        EditUserModal,
        Accordion
    },
    data() { 
        return {
            user: {},
            favorites: [{}],
            editModal: false
        }
    },
    mounted() {
        this.fetchUser();
        this.fetchFavorites();
    },
    methods: {
        safeAge(rawDate){
            console.log(rawDate)
            const safeAge = this.$moment(rawDate, "MM/DD/YYYY").fromNow(true) + ' old';
            return safeAge;
        },
        fetchUser() {
           const url = 'http://localhost:5000/user/1';
           this.$http.get(url)
           .then((result) => {
               this.user = result.data[0]
           }) 
            .catch((error) => {
                console.log(error.response);
            });
        },
        fetchFavorites(){
            const url = 'http://localhost:5000/favorites/1';
            this.$http.get(url)
            .then((result) => {
                console.log(result.data)
                this.favorites = result.data
            })
        },
        showDetails(){
            console.log("AHHH");
        },
        editUser(e){
            console.log(e)
            
        },
        logOut() {
            this.$localStorage.authToken = false;
            this.$router.push('/');
        }
    }

};
</script>
<style>
</style>
