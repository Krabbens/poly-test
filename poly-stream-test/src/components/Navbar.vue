<template>
    <!-- nav - start -->
    <div
        class="sticky top-0 z-40 w-full backdrop-blur flex-none transition-colors duration-500 lg:z-50 lg:border-b lg:border-slate-900/10 dark:border-slate-50/[0.06] bg-white/95 supports-backdrop-blur:bg-white/60 dark:bg-transparent">
        <div class="max-w-8xl mx-auto">
            <div class="py-4 border-b border-slate-900/10 lg:px-8 lg:border-0 dark:border-slate-300/10 mx-4 lg:mx-0">
                <div class="relative flex items-center">
                    <div class="mr-3 flex-none w-[2.0625rem] font-semibold overflow-hidden md:w-auto text-slate-700 dark:text-slate-200 text-lg select-none">polyflow</div>
                    <div class="relative hidden lg:flex items-center ml-auto">
                        <nav class="text-lg leading-6 font-semibold text-slate-700 dark:text-slate-200">
                            <ul class="flex space-x-8">
                                <li><a class="hover:text-indigo-500 dark:hover:text-indigo-400" href="/showcase">log in</a>
                                </li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
            <hr />
        </div>
    </div>
    <!-- nav - end -->
</template>

<script>
export default {
    name: 'Navbar',
    data() {
        return {}
    }
}
</script>