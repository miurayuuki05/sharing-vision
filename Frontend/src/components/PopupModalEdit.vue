<script setup>
import { ref, watch, defineProps, defineEmits } from 'vue';
import axios from 'axios';

const props = defineProps({
    show: Boolean,
    title: String,
    content: String,
    data: Object,
});

const emit = defineEmits(['update:show', 'updated']);

const formData = ref({ ...props.data });

watch(() => props.data, (newData) => {
    formData.value = { ...newData };
}, { deep: true });

const closeModal = () => {
    emit('update:show', false);
    data = {};
};

const updateArticle = async () => {
    try {
        await axios.put(`http://127.0.0.1:5000/article/${formData.value.id}`, formData.value);
        emit('update:show', false);
        emit('updated', formData.value);
        location.reload();
    } catch (error) {
        console.error("Error updating article:", error);
    }
};
</script>

<template>
    <div class="modal" v-show="show">
        <div class="modal-content">
            <span class="close" @click="closeModal">&times;</span>
            <h2>{{ title }}</h2>

            <div v-show="formData">
                <form @submit.prevent="updateArticle">
                    <input type="text" v-model="formData.title" placeholder="Title" />
                    <input type="text" v-model="formData.category" placeholder="Category" />
                    <textarea v-model="formData.content" placeholder="Content"></textarea>
                    <select v-model="formData.status">
                        <option value="draft">Draft</option>
                        <option value="publish">Published</option>
                    </select>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
    /* The Modal (background) */
    .modal {        
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgb(0, 0, 0);
        background-color: rgba(0, 0, 0, 0.4);
        overflow-x :hidden;
    }

    /* Modal Content */
    .modal-content {
        background-color: #fefefe;
        padding: 20px;
        border: 1px solid #888;
        width: calc(100% - 40px);
        height: 100%;
    }

    /* The Close Button */
    .close {
        color: #aaa;
        position: absolute;
        right: 50px;
        font-size: 28px;
        font-weight: bold;
    }

    .close:hover,
    .close:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }

    /* Form Styling */

    form {
        display: flex;
        flex-direction: column;
    }

    input,
    textarea,
    select {
        margin: 10px 0;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    button {
        padding: 10px;
        margin: 10px 0;
        border: none;
        border-radius: 5px;
        background-color: #4CAF50;
        color: white;
        cursor: pointer;
    }

    button:hover {
        background-color: #45a049;
    }

    img {
        width: 100%;
        height: auto;
        margin: 10px 0;
    }

    h2 {
        margin: 10px 0;
    }

    p {
        margin: 10px 0;
    }

    select {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    textarea {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    input[type="text"] {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    input[type="text"]:focus,
    textarea:focus,
    select:focus {
        border-color: #4CAF50;
    }

    input[type="text"]::placeholder,
    textarea::placeholder {
        color: #ccc;
    }


</style>