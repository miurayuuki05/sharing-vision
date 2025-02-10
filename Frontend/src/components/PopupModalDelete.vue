<script setup>
import { ref, watch, defineProps, defineEmits } from 'vue';
import axios from 'axios';

const props = defineProps({
    show: Boolean,    
    data: Object,
});

const emit = defineEmits(['update:show', 'updated']);

const formData = ref({ ...props.data });

watch(() => props.data, (newData) => {
    formData.value = { ...newData };
}, { deep: true });

const closeModal = () => {
    emit('update:show', false);
};

const deleteArticle = async () => {
    try {
        formData.value.status = 'trash';
        await axios.put(`http://127.0.0.1:5000/article/${formData.value.id}`, formData.value);
        emit('update:show', false);
        emit('updated', formData.value);
        location.reload();
    } catch (error) {
        console.error("Error deleting article:", error);
    }
};
</script>

<template>
    <div class="modal" v-show="show">
        <div class="modal-content">
            <span class="close" @click="closeModal">&times;</span>
            <h2>Delete Article</h2>
            <p>Are you sure you want to delete this article?</p>
            <div class="preview">
                <h2>{{ formData.title }}</h2>
                <p>{{ formData.content }}</p>
            </div>

            <div v-show="formData">
                <form @submit.prevent="deleteArticle">
                    <button type="submit">Delete</button>
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
    }

    /* Modal Content */
    .modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
    }

    /* The Close Button */
    .close {
        color: #aaa;
        float: right;
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

    .preview {
        margin: 10px 0;
        padding: 10px;
    }

    .preview h2 {
        margin: 0;
    }

    .preview p {
        margin: 0;
    }


</style>