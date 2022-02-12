<template>
  <span
    class="chat-post"
    :style="{color: `#${color}`}"
  >
    <slot />
  </span>
</template>

<script>
import chatFormatMixin from "./chat-format-mixin";
export default {
  name: 'ChatPost',
  mixins: [chatFormatMixin],
}
</script>
