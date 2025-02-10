<script setup>
import { ref } from 'vue';
import axios from 'axios';

const addArticle = async() =>{
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    const category = document.getElementById('category').value;
    const status = document.querySelector('select[name="status"]').value;

    const article = {
        title,
        content,
        category,
        status
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/article', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(article)
        });
        location.replace('/');
    } catch (error) {
        console.error('Error adding article:', error);
    }
}
</script>

<template>
    <div class="add-article-container">
        <h1>Add Article</h1>
        <form @submit.prevent="addArticle">
            <div class="item-form">
                <label for="title">Title</label>
                <input type="text" id="title" />
            </div>
            <div class="item-form">
                <label for="content">Content</label>
                <textarea id="content"></textarea>
            </div>
            <div class="item-form">
                <label for="category">Category</label>
                <input type="text" id="category" />
            </div>
            <select name="status">
                <option value="draft">Draft</option>
                <option value="publish">Published</option>
            </select>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<style scoped>
    .add-article-container {
        padding: 20px;
        width: calc(100% - 100px);
    }

    .item-form {
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
    }

    h1 {
        margin-bottom: 20px;
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    label {
        font-weight: bold;
    }

    input,
    textarea {
        padding: 5px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }

    button {
        padding: 5px 10px;
        border-radius: 5px;
        border: none;
        background: #3498db;
        color: #fff;
        cursor: pointer;
    }

    button:hover {
        background: #2980b9;
    }

    select {
        padding: 5px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }

    select:focus {
        outline: none;
    }

    select option {
        padding: 5px;
    }

    select option:hover {
        background: #f1f1f1;
    }

    select option:checked {
        background: #f1f1f1;
    }

    select option:focus {
        background: #f1f1f1;
    }

    select option:active {
        background: #f1f1f1;
    }

    select option:selected {
        background: #f1f1f1;
    }

</style>