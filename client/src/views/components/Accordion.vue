<template>
    <div role="tablist">
        <b-card no-body>
        <b-card-header header-tag="header" class="p-2" role="tab">
            <b-button :class="isComplete ? 'complete' : 'incomplete'" block v-b-toggle="'accordion-' + index" variant="info">{{ obj.name }}</b-button>
        </b-card-header>
        <b-collapse :id="'accordion-' + index" accordion="my-accordion" role="tabpanel">
            <b-card-body>
            <b-card-text>{{ obj.description }}</b-card-text>                              
            </b-card-body>
        </b-collapse>
        </b-card>
    </div>

    
</template>

<script>
export default {
    name: 'accordion',
    props: [
        'obj',
        'index'
    ],
    computed: {
        isComplete() {
            if(this.$route.name == 'profile'){
                return true
            }
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