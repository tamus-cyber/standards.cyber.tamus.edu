// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Texas A&M University System Cybersecurity Standards',
  //tagline: 'Dinosaurs are cool',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://standards.cyber.tamus.edu',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'tamus-cyber', // Usually your GitHub org/user name.
  projectName: 'standards.cyber.tamus.edu', // Usually your repo name.

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/tamus-cyber/standards.cyber.tamus.edu/tree/main/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          // 'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  plugins: [
    'docusaurus-lunr-search',
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Cybersecurity Standards',
        logo: {
          alt: 'Texas A&M System Cybersecurity Logo',
          src: 'img/tamus-logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'catalogSidebar',
            position: 'left',
            label: 'Control Standards Catalog',
          },
          {
            type: 'docSidebar',
            sidebarId: 'guidelinesSidebar',
            position: 'left',
            label: 'Guidelines',
          },
          {
            type: 'docSidebar',
            sidebarId: 'resourcesSidebar',
            position: 'left',
            label: 'Resources',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/tamus-cyber/standards.cyber.tamus.edu',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        links: [
          {
            title: 'Required Links',
            items: [
              {
                label: 'State of Texas',
                href: 'https://www.texas.gov/',
              },
              {
                label: 'Texas Homeland Security',
                href: 'https://gov.texas.gov/organization/hsgd',
              },
              {
                label: 'Texas Veterans Portal',
                href: 'https://veterans.portal.texas.gov/',
              },
              {
                label: 'Risk, Fraud & Misconduct Hotline',
                href: 'https://secure.ethicspoint.com/domain/media/en/gui/19681/index.html',
              },
              {
                label: 'Privacy',
                href: 'https://www.tamus.edu/marcomm/reports/privacy/',
              },
              {
                label: 'State Link Policy',
                href: 'https://dir.texas.gov/resource-library-item/state-website-linking-privacy-policy?id=21',
              },
              {
                label: 'Web Accessibility',
                href: 'https://www.tamus.edu/marcomm/reports/accessibility/',
              },
              {
                label: 'Campus Carry',
                href: 'https://www.tamus.edu/system/campus-carry-rules/',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} The Texas A&M University System. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
