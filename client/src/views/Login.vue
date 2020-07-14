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
                                <base-input alternative
                                            class="mb-3"
                                            placeholder="Email"
                                            addon-left-icon="ni ni-email-83"
                                            :value="input.username" 
                                            @input="val => { input.username = val }"
                                            >
                                </base-input>
                                <base-input alternative
                                            type="password"
                                            placeholder="Password"
                                            addon-left-icon="ni ni-lock-circle-open"
                                            :value="input.password"
                                            @input="val => { input.password = val }"
                                            >
                                </base-input>
                                <base-checkbox
                                    @input="val => { input.remember = val }">
                                    Remember me
                                </base-checkbox>
                                <div class="text-center">
                                    <base-button @click="log" type="primary" class="my-4">Sign In</base-button>
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
        log: function(val) {
            console.log(this.input.username)
            console.log(this.input.password)
            console.log(this.input.remember)
        }
    }
}
</script>
<style>
</style>
