<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const articles = ref([])

const showModal = ref(false)

const showDeleteModal = ref(false)

const selectedArticle = ref(null);

const tab1 = ref(true)
const tab2 = ref(false)
const tab3 = ref(false)
const tab4 = ref(false)

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


const allArticlesExceptTrash = computed(() => {
  return articles.value.filter(article => article.status !== 'trash');
});

const draftArticles = computed(() => {
  return articles.value.filter(article => article.status === 'draft');
});

const publishedArticles = computed(() => {
  return articles.value.filter(article => article.status === 'publish');
});

const trashArticles = computed(() => {
  return articles.value.filter(article => article.status === 'trash');
});

const openEditModal = (article) => {
  selectedArticle.value = article;
  showModal.value = true;
};

const openDeleteModal = (article) => {
  selectedArticle.value = article;
  showDeleteModal.value = true;
};

</script>

<template>
    <div class="table-container">

      <nav>
        <button @click="tab1 = true; tab2 = false; tab3 = false; tab4 = false" :class="{ active: tab1 }">All</button>
        <button @click="tab1 = false; tab2 = true; tab3 = false; tab4 = false" :class="{ active: tab2 }">Draft</button>
        <button @click="tab1 = false; tab2 = false; tab3 = true; tab4 = false" :class="{ active: tab3 }">Published</button>
        <button @click="tab1 = false; tab2 = false; tab3 = false; tab4 = true" :class="{ active: tab4 }">Trash</button>
      </nav>

      <table v-show="tab1">
        <thead>
          <tr>
            <th>No</th>
            <th>Title</th>
            <th>Category</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(article, index) in allArticlesExceptTrash" :key="article.id">
            <td>{{ index + 1 }}</td>
            <td>{{ article.title }}</td>
            <td>{{ article.category }}</td>
            <td>
                <button class="edit-btn" @click="openEditModal(article)">Edit</button>
                <button class="delete-btn" @click="openDeleteModal(article)">Delete</button>
            </td>
            <popup-modal-edit :show="showModal" @update:show="showModal = $event" :title="article.title" :content="article.content" :data="selectedArticle" />
            <popup-modal-delete :show="showDeleteModal" @update:show="showDeleteModal = $event" :data="selectedArticle" />
          </tr>
        </tbody>
      </table>

      <table v-show="tab2">
        <thead>
          <tr>
            <th>No</th>
            <th>Title</th>
            <th>Category</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(article, index) in draftArticles" :key="article.id">
            <td>{{ index + 1 }}</td>
            <td>{{ article.title }}</td>
            <td>{{ article.category }}</td>
            <td>
                <button class="edit-btn" @click="showModal = true">Edit</button>
                <button class="delete-btn" @click="showDeleteModal = true">Delete</button>
            </td>
            <popup-modal-edit :show="showModal" @update:show="showModal = $event" :title="article.title" :content="article.content" :data="selectedArticle" />
            <popup-modal-delete :show="showDeleteModal" @update:show="showDeleteModal = $event" :data="selectedArticle" />
          </tr>
        </tbody>
      </table>

      <table v-show="tab3">
        <thead>
          <tr>
            <th>No</th>
            <th>Title</th>
            <th>Category</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(article, index) in publishedArticles" :key="article.id">
            <td>{{ index + 1 }}</td>
            <td>{{ article.title }}</td>
            <td>{{ article.category }}</td>
            <td>
                <button class="edit-btn" @click="showModal = true">Edit</button>
                <button class="delete-btn" @click="showDeleteModal = true">Delete</button>
            </td>
            <popup-modal-edit :show="showModal" @update:show="showModal = $event" :title="article.title" :content="article.content" :data="article" />
            <popup-modal-delete :show="showDeleteModal" @update:show="showDeleteModal = $event" :data="article" />
          </tr>
        </tbody>
      </table>

      <table v-show="tab4">
        <thead>
          <tr>
            <th>No</th>
            <th>Title</th>
            <th>Category</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(article, index) in trashArticles" :key="article.id">
            <td>{{ index + 1 }}</td>
            <td>{{ article.title }}</td>
            <td>{{ article.category }}</td>
            <td>
                <button class="edit-btn" @click="showModal = true">Edit</button>
            </td>
            <popup-modal-edit :show="showModal" @update:show="showModal = $event" :title="article.title" :content="article.content" :data="article" />
            <popup-modal-delete :show="showDeleteModal" @update:show="showDeleteModal = $event" :data="article" />
          </tr>
        </tbody>
      </table>
      

    </div>
  </template>
  
  <style scoped>
  /* Table Container */
  .table-container {
    padding: 20px;
    width: calc(100% - 100px);
  }
  
  /* Table Styling */
  table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    overflow-x: auto;
  }
  
  /* Table Header */
  thead {
    background: #2c3e50;
    color: white;
  }
  
  th {
    padding: 12px 16px;
    text-align: left;
    font-weight: 600;
  }
  
  /* Table Body */
  tbody tr {
    border-bottom: 1px solid #ddd;
    transition: background 0.3s ease-in-out;
  }
  
  tbody tr:hover {
    background: #f3f4f6;
  }
  
  td {
    padding: 12px 16px;
    color: #333;
  }
  
  /* Buttons */
  button {
    padding: 6px 12px;
    margin: 4px;
    border-radius: 5px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
  }
  
  /* Edit Button */
  .edit-btn {
    background: #3498db;
    color: white;
    border: none;
  }
  
  .edit-btn:hover {
    background: #2980b9;
  }
  
  /* Delete Button */
  .delete-btn {
    background: #e74c3c;
    color: white;
    border: none;
  }
  
  .delete-btn:hover {
    background: #c0392b;
  }

  /* Active Tab */

  button.active {
    background: #3498db;
    color: white;
  }


  </style>
  