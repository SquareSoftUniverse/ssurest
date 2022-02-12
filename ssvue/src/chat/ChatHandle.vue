<template>
  <span
    class="chat-post-handle"
    :style="{color: `#${color}`}"
  >
    <slot />
  </span>
</template>

<script>
import chatFormatMixin from "./chat-format-mixin";
export default {
  name: 'ChatHandle',
  mixins: [chatFormatMixin],
}
</script>

<style scoped>
.chat-post-handle {
  font-weight: bold;
}
</style>