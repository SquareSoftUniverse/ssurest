module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ["plugin:vue/vue3-essential", "eslint:recommended", "@vue/prettier"],
  parserOptions: {
    parser: "babel-eslint",
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "array-bracket-spacing": [
      "error",
      "always",
      {
        singleValue: false,
      },
    ],
    "no-multi-spaces": ["warn"],
    "no-unused-vars": ["warn"],
    "space-before-function-paren": [ "warn", "never" ],
  },
};
