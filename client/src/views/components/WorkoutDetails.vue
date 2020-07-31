<template>
    <div>
        <div class="container">
            <div class="row">

                <div class="card p-2" style="width: 18rem;">
                    <img class="card-img-top" src="/img/brand/chest-test.jpg" alt="Card image cap">
                    <div class="card-body">
                        <p class="card-text">{{ workout.name }}</p>
                    </div>
                </div>
                    
                <div class="col">
                    <div class="text-left">
                        <ul class="list-group">
                            <li class="list-group-item"> <b>Average Rating:</b> {{ workout.rating }} </li>
                            <li class="list-group-item"> <b>Description:</b> {{ workout.description }} </li>
                            <li class="list-group-item"> <b>Weight:</b> {{ workout.adv_wt }} </li>
                            <li class="list-group-item"> <b>Reps:</b> {{ workout.adv_reps}} </li>
                            <li class="list-group-item col-med"> <b>Set:</b> {{ setNum }} of <b>{{ workout.sets }}</b>
                                <div class="float-right">
                                    <button @click="addSet" type="button" class="btn btn-primary btn-arrow-up"><b>+</b></button>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'workout-details',
    props: [
        'workout'
    ],
    data() {
        return {
            setNum: 0
        }
    },
    methods: {
        addSet(){
            if(this.setNum == this.workout.sets) { return }
            this.setNum += 1;
            if(this.setNum >= this.workout.sets){
                this.$emit('complete');
                return
            }
        }
    }
}
</script>


<style lang="scss" scoped>

</style>