<template>
    <div class="bg-black min-w-max min-h-screen overflow-hidden ">
        <div class="absolute h-max blur-3xl opacity-20 overflow-hidden rounded-lg bg-gray-100 lg:h-auto w-screen">
            <img src="../assets/home-coverart.jpg" loading="lazy" alt="Landing cover art"
                class="relative z-0 h-screen w-screen object-cover object-center" />
        </div>
        <div class="relative mx-auto max-w-screen-2xl px-4 md:px-8">
            <header class="mb-8 flex items-center justify-between md:pt-8">
                <Navbar />
            </header>

            <section class="flex flex-col justify-between gap-6 sm:gap-10 md:gap-16 lg:flex-row">

                <!--image left panel-->
                <div class="rounded-3xl shadow bg-gray-100 shadow-lg lg:h-auto w-5/12">
                    <img src="../assets/home-coverart.jpg" loading="lazy" alt="Landing cover art"
                        class="rounded-xl h-full w-full object-cover object-center" />
                </div>
                <!--text right panel-->
                <div class="flex flex-col justify-between xl:w-1/2 items-center">
                    <div class="sm:text-center lg:py-12 lg:text-left xl:py-24">
                        <h1 class="select-none mb-8 text-4xl font-bold text-slate-100 sm:text-5xl md:mb-12 md:text-6xl">simple music player
                        </h1>
                        <p class="select-none mb-48 font-semibold text-slate-200 md:text-lg xl:text-xl">spotify, yt, soundcloud
                        </p>

                        <div class="flex flex-col gap-2.5 sm:flex-row sm:justify-center lg:justify-start">
                            <router-link to="/login"
                                class="inline-block rounded-lg bg-indigo-700 px-8 py-3 text-center text-sm font-semibold text-white outline-none ring-indigo-300 transition duration-100 hover:bg-indigo-600 focus-visible:ring active:bg-indigo-700 md:text-base cursor-pointer">Log
                                in</router-link>

                            <a href="#"
                                class="inline-block rounded-lg bg-gray-200 px-8 py-3 text-center text-sm font-semibold text-gray-900 outline-none ring-purple-300 transition duration-100 hover:bg-gray-300 focus-visible:ring active:text-gray-700 md:text-base">Register</a>
                        </div>
                    </div>
                </div>

            </section>
            <Footer />
        </div>



    </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
export default {
    name: 'Home',
    data() {
        return {
            text: 'Hello world!'
        }
    },
    components: {
        Navbar,
        Footer
    }
}
</script>