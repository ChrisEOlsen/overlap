module.exports = {
  mode: "jit",
  content: [
    "./app/templates/**/*.html", // HTML files
    "./app/**/*.py", // Python files
    "./app/**/*.js", // JavaScript files
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark", "business", "night"],
  },
}
