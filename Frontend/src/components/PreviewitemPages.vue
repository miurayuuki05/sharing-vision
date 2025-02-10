<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const article = ref([])

const id = ref(window.location.pathname.split('/').pop())

onMounted(async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/article/' + id.value);
        console.log(id.value); // Check the actual data
        article.value = response.data; // Assign only if data is present
    } catch (error) {
        console.error('Error fetching articles:', error);
    }

    console.log('Articles:', article.value);
});
        
</script>

<template>
    <div class="preview-article-container">
        <div class="article-container">
            <div v-if(article) :key="article.id">
                <h3 class="article-title">{{ article.title }}</h3>
                <div class="article-content">
                    <p>{{ article.content }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .preview-article-container {
        padding: 20px;
        width: calc(100% - 200px);
    }

    .article-container {
        display: flex;
        flex-wrap: wrap;
    }

    .article-title {
        font-size: 24px;
        font-weight: bold;
    }

    .article-content {
        margin-top: 20px;
    }

    .article-content p {
        font-size: 18px;
    }
    
</style>