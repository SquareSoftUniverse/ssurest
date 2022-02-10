<template>
  <div class="chat-post">
    <span class="chat-post-handle" :style="{color: `#${post.handle.handle_color}`}">{{ post.handle.name }}:&nbsp;</span>
    <span class="chat-post-datetime" :style="{color: `#${post.handle.text_color}`}">({{ post.datetime_posted }})&nbsp;</span>
    <span class="chat-post" :style="{color: `#${post.handle.text_color}`}">{{ post.message }}</span>
  </div>
</template>

<script>
export default {
  name: "ChatPost",
  props: ['post'],
};
</script>

<style>

</style>
