<template>
    <div>

        <div class="position-relative">
            <!-- shape Hero -->
            <section class="section-shaped my-0">
                <div class="shape shape-style-1 shape-default shape-skew">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                <div class="container shape-container d-flex">
                    <div class="col px-0">
                        <h1 class="display-3  text-white"> Welcome to the Purple Cobras Workout App! 💪 </h1>
                        <p class="lead  text-white">Get ready to burn calories and build muscle like you wouldn't believe.</p>
                            <div class="row">
                                <div class="col-med-3">
                                    <ul class="text-white">
                                        <li> Explore personalized workout routines curated just for you!</li>
                                        <li> Share wourkout routines and tips in our community boards. </li>
                                        <li> Stick to your fitness goals with daily reminders and progress tracking. </li>
                                    </ul>
                                </div>
                                <div class="col-sm float-right">
                                    <img class="rounded" alt="100x100" src="/img/theme/crop-woman-in-activewear-browsing.jpg" data-holder-rendered="true" width="400px">
                                </div>
                            </div>
                    </div>
                </div>
            </section>
        </div>
 
        <section class="section section-lg">
            <div class="container">
                <div class="row justify-content-center text-center mb-3">
                    <div class="col-lg-8 mb-3">
                        <h2 class="display-3">Meet Our Trainers</h2>
                        <p class="lead text-muted">Our Globo Gym experts are here to assist you on your fitness journey!</p>
                    </div>
                </div>
                <div class="row">

                    <div class="col-md-6 col-lg mb-5 mb-lg-0">
                        <div class="px-4">
                            <img v-lazy="'img/theme/white-goodman.jpg'"
                                 class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                                 style="width: 200px;">
                            <div class="pt-4 text-center">
                                <h5 class="title">
                                    <span class="d-block mb-1">White Goodman</span>
                                    <small class="h6 text-muted">CEO Globo Gym</small>
                                </h5>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-6 col-lg mb-lg-0" style="overflow: hidden;">
                        <div class="px-4">
                            <img v-lazy="'img/theme/fran-stalin.jpg'"
                                 class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                                 style="width: 200px;">
                            <div class="pt-4 text-center">
                                <h5 class="title">
                                    <span class="d-block mb-1">Fran Stalinov</span>
                                    <small class="h6 text-muted">Dodgeball Assassin</small>
                                </h5>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-6 col-lg mb-5 mb-lg-0">
                        <div class="px-4">
                            <img v-lazy="'img/theme/jamal-duff.jpg'"
                                 class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                                 style="width: 200px;">
                            <div class="pt-4 text-center">
                                <h5 class="title">
                                    <span class="d-block mb-1">Jamal Duff</span>
                                    <small class="h6 text-muted">Big Muscle Specialist</small>
                                </h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        
        

    </div>
</template>

<script>
export default {
  name: "home",
  components: {}
};
</script>

<style>
#app ul > li {
    padding: 10px;
    margin: 0 0 30px 0
};

</style>
