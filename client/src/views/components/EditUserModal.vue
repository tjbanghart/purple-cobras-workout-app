<template>
    <modal :show.sync="showSync" @close="$emit('close')">
        <template slot="header">
            <h5 class="modal-title" id="exampleModalLabel">Edit Profile</h5>
        </template>
            <div>
                
                    <form role="form">
                        <base-input alternative
                                    class="mb-3"
                                    placeholder="User Name"
                                    addon-left-icon="ni ni-circle-08"
                                    v-model="user.username"
                                    >
                                </base-input>
                                <base-input class="mb-3" addon-left-icon="ni ni-calendar-grid-58" >
                                    <flat-picker slot-scope="{focus, blur}"
                                                @on-open="focus"
                                                @on-close="blur"
                                                :config="{allowInput: true}"
                                                class="form-control datepicker"
                                                v-model="user.birthdate"
                                                placeholder="Birthdate"
                                                >
                                    </flat-picker>
                                </base-input>
                            </form>
                       
            </div>
        <template slot="footer">
            <base-button type="secondary" @click="$emit('close')">Close</base-button>
            <base-button type="primary" @click="$emit('save', user)">Save changes</base-button>
        </template>
    </modal>
</template>

<script>
import  Modal  from '@/components/Modal.vue'
import flatPicker from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

export default {
    name: "edit-user-modal",
    components: {
        Modal,
        flatPicker
    },
    props: [
        'userInfo',
        'showSync'
    ],
    computed: {
        user: function() {
            return Object.assign({}, this.userInfo)
        }
    },


}
</script>