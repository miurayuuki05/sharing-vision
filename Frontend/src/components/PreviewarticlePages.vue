<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';

const articles = ref([]);

onMounted(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/article/10/0');
      console.log('Response Data:', response.data); // Check the actual data
  
      if (response.data) {
        console.log('Data received from API:', response.data);
        articles.value = response.data; // Assign only if data is present
      } else {
        console.error('No data received from API');
      }
    } catch (error) {
      console.error('Error fetching articles:', error);
    }
});

const publishedArticles = computed(() => {
  return articles.value.filter(article => article.status === 'publish');
});

</script>

<template>  
    <div class="preview-article-container">
        <h2>Published Articles</h2>
        <div class="articleContainer">
        <div v-for="article in publishedArticles" :key="article.id">
        <a :href="'/preview/' + article.id" class="article-link">
            <div class="article-item">
                <h3>{{ article.title }}</h3>
                <p>{{ article.content }}</p>
            </div>
        </a>
        </div>
        </div>
    </div>
</template>

<style scoped>
    .preview-article-container {
        padding: 20px;
        width: calc(100% - 200px);
    }

    .articleContainer {
        display: flex;
        flex-wrap: wrap;
    }
    .article-item {
        width: 200px;
        height: 130px;
        margin: 10px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .article-item h3 {
        margin: 0;
    }

    .article-item p {
        overflow-wrap: break-word;
        word-wrap: break-word;
        hyphens: auto;
    }

    .article-link {
        text-decoration: none;
        color: inherit;
    }

    .article-link:hover .article-item {
        background-color: #f9f9f9;
    }

    .article-link:hover .article-item h3 {
        color: #3498db;
    }
</style>


