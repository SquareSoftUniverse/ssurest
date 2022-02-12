module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    "plugin:vue/vue3-essential",
    "plugin:vue/vue3-recommended",
    "eslint:recommended",
  ],
  parserOptions: {
    parser: "babel-eslint",
  },
  rules: {
    "array-bracket-spacing": [
      "error",
      "always",
      {
        singleValue: false,
      },
    ],
    indent: ["warn", 2],
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-multi-spaces": ["warn"],
    "no-unused-vars": ["warn"],
    "space-before-function-paren": ["warn", "never"],
  },
};

