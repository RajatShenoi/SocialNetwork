/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html, js}",
    "./accounts/templates/**/*.{html, js}",
    "./static/**/*.{html, js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
  ],
  daisyui: {
    themes: [
      "dark",
    ]
  },
}

