<template>
<div>
   <div>
        <section class="section-profile-cover section-shaped my-0">
            <div class="shape shape-style-3 shape-primary">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </section>
    </div>
    <section class="section pt-0">
    <div class="container">
        <card class="card mt--300" no-body>
            <div>
                <div class="justify-content-center">
                    <div class="card-header">
                        <ul class="nav nav-tabs" id="myTab" role="tablist">
                            <li class="nav-item" v-for="(group, index) in groups" :key="index">
                                <a 
                                class="nav-link"
                                :id="group" 
                                data-toggle="tab" 
                                :href="'#' + group"  
                                role="tab"
                                >{{ group }}
                                </a>    
                            </li>
                        </ul>
                    </div>
                    
                    <div class="text-center">
                        <div class="row justify-content-center">
                            <div class="col-lg">
                                <accordion 
                                v-for="(workout, index) in workouts" :key="index"
                                :obj="workout"
                                :index="index"
                                > 
                                </accordion>
                            </div>
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
import Accordion from './components/Accordion'
export default {
    components: {
        Accordion
    },
    data() {
        return {
            workouts: [],
            groups: [
                'Chest',
                'Back',
                'Legs',
                'Arms',
                'Abs'
            ]
        }
    },
    mounted() {
        this.fetchWorkouts()
    },
    methods: {
        fetchWorkouts() {
            const url = 'http://localhost:5000/allworkouts';
            this.$http.get(url)
            .then((results) => {
                console.log(results.data)
                this.workouts = results.data;
            })
        }
    }

    
}
</script>


<style lang="scss" scoped>

</style>