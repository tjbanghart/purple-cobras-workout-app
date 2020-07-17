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
                                            placeholder="Name"
                                            addon-left-icon="fa fa-user-circle"
                                            :value="input.name"
                                            @input="val => { input.name = val }"
                                            >
                                </base-input>
                                <base-input alternative
                                            class="mb-3"
                                            placeholder="Email"
                                            addon-left-icon="ni ni-email-83"
                                            :value="input.email"
                                            @input="val => { input.email = val }"
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
                                <base-checkbox @input="val => { input.policy = val }">
                                    <span>I agree with the
                                        <a href="#">Privacy Policy</a>
                                    </span>
                                </base-checkbox>
                                <div class="text-center">
                                    <base-button type="primary" class="my-4" @click="log">Create account</base-button>
                                </div>
                            </form>
                        </template>
                    </card>
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
                name: "",
                email: "",
                password: "",
                policy: false
            }
        }
    },
    methods: {
        log: function(val) {
            console.log(this.input.name)
            console.log(this.input.email)
            console.log(this.input.password)
            console.log(this.input.policy)
        }
    }
}
</script>
<style>
</style>
