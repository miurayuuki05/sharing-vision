<script setup>
    import { onMounted, ref } from 'vue'

    const sidebarItems = ref([
        {
            title: 'Articles',
            to: '/'
        },
        {
            title: 'Add Article',
            to: '/add-article'
        },
        {
            title: 'Preview',
            to: '/preview'
        },
    ])

    const path = ref(window.location.pathname)

    
</script>

<template>
    <nav class="sidebar">
        <ul>
            <li v-for="item in sidebarItems" :key="item.title" :class="{ active: item === activeItem }">
                <a :href="item.to" @click="activeItem = item">
                    <span>{{ item.title }}</span>
                </a>
            </li>
        </ul>
    </nav>
</template>

<style scoped>
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 200px;
    background: #2c3e50;
    color: #fff;
    padding-top: 20px;
}

.sidebar ul {
    list-style: none;
    padding: 0;
}

.sidebar li {
    padding: 10px 20px;
    cursor: pointer;
    transition: background 0.3s;
}

.sidebar li:hover {
    background: #34495e;
}

.sidebar li.active {
    background: #34495e;
}

.sidebar a {
    display: flex;
    align-items: center;
    color: #fff;
    text-decoration: none;
    font-size: x-large;
}

.sidebar a span {
    margin-left: 10px;
}

.sidebar a:hover {
    color: #fff;
}

.sidebar a.active {
    color: #fff;
}

</style>