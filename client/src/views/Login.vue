<template>
    <section class="section section-shaped section-lg my-0">
        <div class="shape shape-style-1 bg-gradient-default">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
        <div class="container pt-lg-md">
            <div class="row justify-content-center">
                <div class="col-lg-5">
                    <card type="secondary" shadow
                          header-classes="bg-white pb-5"
                          body-classes="px-lg-5 py-lg-5"
                          class="border-0">
                        <template>
                            <form role="form">
                                <base-input 
                                    alternative
                                    class="mb-3"
                                    placeholder="Username"
                                    addon-left-icon="ni ni-circle-08"
                                    v-model="input.username"
                                    >
                                </base-input>
                                <!-- <base-input 
                                    alternative
                                    type="password"
                                    placeholder="Password"
                                    addon-left-icon="ni ni-lock-circle-open"
                                    v-model="input.password"
                                    >
                                </base-input> -->
                                <!-- <base-checkbox
                                    v-model="input.remember"
                                    >
                                    Remember me
                                </base-checkbox> -->
                                <div class="text-center">
                                    <base-button @click="auth" type="primary" class="my-4">Sign In</base-button>
                                </div>
                            </form>
                        </template>
                    </card>
                    <div class="row mt-3">
                        <div class="col-6">
                            <a href="#" class="text-light">
                                <small>Forgot password?</small>
                            </a>
                        </div>
                        <div class="col-6 text-right">
                            <router-link to="/register" class="text-light">
                                <small>Create new account</small>
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
export default {
    data() {
        return {
            input: {
                username: "",
                password: "",
                remember: false
            }
        }
    },
    methods: {
        auth: function(e) {
            const url = `http://localhost:5000/user/${this.input.username}`
            this.$http.get(url) 
            .then((results) => {
                console.log(results.data)
                if(results.data.length < 1) {
                    alert('I don\'t know that user. Maybe register that name?')
                    this.$router.push('/register');
                    return;
                }
                this.$localStorage.authToken = true;
                this.$localStorage.username = results.data[0].username
                this.$localStorage.user_id = results.data[0].user_id
                this.$router.push('/profile');
            })
        },
    }
}
</script>
<style>
</style>
