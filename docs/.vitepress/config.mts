import { defineConfig } from "vitepress";
import markdownIt from "markdown-it";
import markdownKatex from "markdown-it-katex";
import markdownPlantuml from "markdown-it-plantuml";
import markdownAdmonition from "markdown-it-admonition";
import markdownTaskLists from "markdown-it-task-lists";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Voice of Experts",
  description: "Лабораторні роботи з дисципліни Організація баз даних",
  lang: "uk",
  base: "/db_labs/",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Головна", link: "/" },
      { text: "Зміст", link: "/intro/README" },
      { text: "Автори", link: "/README" },
    ],

    footer: {
      copyright: "MIT Licensed | Copyright © 2025 TockePie"
    },

    search: {
      provider: 'local'
    },

    sidebar: [
      {
        text: "Зміст",
        items: [
          { text: "Вступ", link: "/intro/README" },
          {
            text: "Розроблення загальних вимог до системи",
            items: [
              { text: "Аналіз предметної області", link: "/requirements/state-of-the-art" },
              {
                text: "Потреби зацікавлених сторін",
                link: "/requirements/stakeholders-needs",
              },
            ],
          },
          {
            text: "Розроблення вимог до функціональности системи",
            link: "/use cases/README",
          },
          {
            text: "Проектування інформаційного забезпечення",
            link: "/design/README",
          },
          {
            text: "Реалізація інформаційного та програмного забезпечення",
            link: "/software/README",
          },
          {
            text: "Тестування працездатності системи",
            link: "/test/README",
          },
          {
            text: "Висновки",
            link: "/conclusion/README",
          },
        ],
      },
    ],

    socialLinks: [
      { icon: "github", link: "https://github.com/TockePie/db_labs" },
    ],
  },

  markdown: {
    config: (md) => {
      md.set({ html: true })
      md.use(markdownKatex)
      md.use(markdownPlantuml)
      md.use(markdownAdmonition)
      md.use(markdownTaskLists)
    }
  }
});
