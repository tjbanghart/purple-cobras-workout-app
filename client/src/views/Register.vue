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
                                            v-model="input.username"
                                            >
                                </base-input>
                                <base-input class="mb-3" addon-left-icon="ni ni-calendar-grid-58" >
                                    <flat-picker slot-scope="{focus, blur}"
                                                @on-open="focus"
                                                @on-close="blur"
                                                :config="{allowInput: true}"
                                                class="form-control datepicker"
                                                v-model="input.birthdate"
                                                placeholder="Birthdate"
                                                >
                                    </flat-picker>
                                </base-input>
                                <div class="form-group">
                                    <select class="form-control" id="exampleFormControlSelect1" v-model="input.gender">
                                    <option>Male</option>
                                    <option>Female</option>
                                    <option>Other</option>
                                    </select>
                                </div>
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
import flatPicker from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
export default {
    components: {
        flatPicker
    },
    data() {
        return {
            input: {
                username: "",
                gender: "Male",
                birthdate: ""
            }
        }
    },
    methods: {
        log: function() {
           console.log(this.input)
        }
    }
}
</script>
<style>
</style>
