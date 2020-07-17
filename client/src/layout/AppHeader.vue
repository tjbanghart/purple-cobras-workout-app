<template>
    <header class="header-global">
        <base-nav class="navbar-main" transparent type="" effect="light" expand>
            <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
                <img src="/img/brand/globo-gym.gif" alt="logo" >
            </router-link>

            <div class="row" slot="content-header" slot-scope="{closeMenu}">
                <div class="col-6 collapse-brand">
                    <a href="https://demos.creative-tim.com/vue-argon-design-system/documentation/">
                        <img src="img/brand/blue.png">
                    </a>
                </div>
                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu"></close-button>
                </div>
            </div>

            <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
                <base-dropdown class="nav-item" menu-classes="dropdown-menu-xl">
                    <a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">
                        <i class="ni ni-ui-04 d-lg-none"></i>
                        <span class="nav-link-inner--text">Community</span>
                    </a>
                    <div class="dropdown-menu-inner">
                        <a href="#"
                           class="media d-flex align-items-center">
                            <div class="icon icon-shape bg-gradient-primary rounded-circle text-white">
                                <i class="ni ni-world"></i>
                            </div>
                            <div class="media-body ml-3">
                                <h6 class="heading text-primary mb-md-1">Community Boards</h6>
                                <p class="description d-none d-md-inline-block mb-0">Share and learn about new workout routines 
                                    in our community message boards.</p>
                            </div>
                        </a>
                        <a href="#"
                           class="media d-flex align-items-center">
                            <div class="icon icon-shape bg-gradient-warning rounded-circle text-white">
                                <i class="ni ni-trophy"></i>
                            </div>
                            <div class="media-body ml-3">
                                <h5 class="heading text-warning mb-md-1">Leaderboards</h5>
                                <p class="description d-none d-md-inline-block mb-0">See how you stack up against
                                    other fitness addicts.
                                </p>
                            </div>
                        </a>
                    </div>
                </base-dropdown>
                <base-dropdown class="nav-item" menu-classes="dropdown-menu-xl">
                    <a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">
                        <span class="nav-link-inner--text">Workout</span>
                    </a>
                    <div class="dropdown-menu-inner">
                        <a href="#"
                           class="media d-flex align-items-center">
                            <div class="icon icon-shape bg-gradient-primary rounded-circle text-white">
                                <i class="ni ni-user-run"></i>
                            </div>
                            <div class="media-body ml-3">
                                <h6 class="heading text-primary mb-md-1">Daily Workout</h6>
                                <p class="description d-none d-md-inline-block mb-0">Target each muscle group using with one of our daily workout routines. Curated just for you!</p>
                            </div>
                        </a>
                        <a href="#"
                           class="media d-flex align-items-center">
                            <div class="icon icon-shape bg-gradient-warning rounded-circle text-white">
                                <i class="fa fa-book"></i>
                            </div>
                            <div class="media-body ml-3">
                                <h5 class="heading text-warning mb-md-1">Past Workouts</h5>
                                <p class="description d-none d-md-inline-block mb-0">See your previous workout history.</p>
                            </div>
                        </a>
                    </div>
                </base-dropdown>
            </ul>
            <ul class="navbar-nav align-items-lg-center ml-lg-auto">
                
                <li class="nav-item d-none d-lg-block ml-lg-4">
                    <router-link to="/login" class="btn btn-neutral btn-icon">
                <span class="btn-inner--icon">
                  <i class="fa fa-user-circle mr-2" aria-hidden="true"></i>
                </span>
                        <span class="nav-link-inner--text">Log in/Sign Up</span>
                    </router-link>
                </li>
            </ul>
        </base-nav>
    </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";

export default {
  components: {
    BaseNav,
    CloseButton,
    BaseDropdown
  }
};
</script>
<style lang="scss">

#app .navbar-brand  img {
    width: 120px; 
    height: 120px;
};

</style>
