import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

// Components
import TableArticle from './components/TableArticle.vue'
import SidebarNav from './components/SidebarNav.vue'
import PopupModalEdit from './components/PopupModalEdit.vue'
import PopupModalDelete from './components/PopupModalDelete.vue'
import PreviewarticlePages from './components/PreviewarticlePages.vue'
import AddarticlePages from './components/AddarticlePages.vue'
import PreviewitemPages from './components/PreviewitemPages.vue'

const app = createApp(App);
app.component('TableArticle', TableArticle);
app.component('SidebarNav', SidebarNav);
app.component('PopupModalEdit', PopupModalEdit);
app.component('PopupModalDelete', PopupModalDelete);
app.component('PreviewarticlePages', PreviewarticlePages);
app.component('AddarticlePages', AddarticlePages);
app.component('PreviewitemPages', PreviewitemPages);
app.mount('#app');


