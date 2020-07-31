<template>
    <div role="tablist">
        <b-card no-body>
        <b-card-header header-tag="header" class="p-2" role="tab">
            <b-button :class="isComplete ? 'complete' : 'incomplete'" block v-b-toggle="'accordion-' + index" variant="info">{{ obj.name }}</b-button>
        </b-card-header>
        <b-collapse :id="'accordion-' + index" accordion="my-accordion" role="tabpanel">
            <b-card-body>
                <workout-details @complete="complete" :workout="obj"></workout-details>
            </b-card-body>
        </b-collapse>
        </b-card>
    </div>    
</template>

<script>
import WorkoutDetails from './WorkoutDetails'
export default {
    name: 'accordion',
    components: {
        WorkoutDetails
    },
    props: [
        'obj',
        'index'
    ],
    data(){
        return {
            isComplete: false
        }
    },
    mounted() {
        if(this.$route.name == 'profile')
        this.isComplete = true
    },
    methods: {
        complete(){
            return this.isComplete = true
        }
    }
    
}
</script>

<style lang="scss" scoped>
.incomplete {
    background-color: rgb(255, 60, 0);
}

.complete {
    background-color: steelblue;
}


</style>