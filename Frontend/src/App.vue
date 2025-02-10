<script setup>
import { ref, onMounted } from 'vue'

const pathUrl = ref(window.location.pathname)

const showMainTab = ref(true)
const showPreviewTab = ref(false)
const showPreviewitemTab = ref(false)
const showAddTab = ref(false)

onMounted(() => {
  if (pathUrl.value === '/') {
    showMainTab.value = true
    showPreviewTab.value = false
    showPreviewitemTab.value = false
    showAddTab.value = false
  } else if (pathUrl.value === '/preview') {
    showMainTab.value = false
    showPreviewTab.value = true
    showPreviewitemTab.value = false
    showAddTab.value = false
  } else if (pathUrl.value === '/add-article') {
    showMainTab.value = false
    showPreviewTab.value = false
    showPreviewitemTab.value = false
    showAddTab.value = true
  } else {
    showMainTab.value = false
    showPreviewTab.value = false
    showPreviewitemTab.value = true
    showAddTab.value = false
  }
})



</script>

<template>
  <main>
    <div class="container" id="main-tab" v-show="showMainTab">
      <SidebarNav />
      <TableArticle />
    </div>
    <div class="container" id="preview-tab" v-show="showPreviewTab">
      <SidebarNav />
      <PreviewarticlePages />
    </div>
    <div class="container" id="add-tab" v-show="showAddTab">
      <SidebarNav />
      <AddarticlePages />
    </div>
    <div class="container" id="previewitem-tab" v-show="showPreviewitemTab">
      <SidebarNav />
      <PreviewitemPages />
    </div>

  </main>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  width: calc(100% - 200px);
  justify-content: end;
  align-items: end;
}
main {
  display: flex;
  justify-content: end;
  align-items: end;
  width: 100%;
}
</style>
