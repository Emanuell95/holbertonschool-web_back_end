// eslint.config.js
import js from '@eslint/js';
import eslintPluginJest from 'eslint-plugin-jest';
import { flatConfigs } from 'eslint-config-airbnb-base';

export default [
  js.configs.recommended,
  ...flatConfigs,
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
      globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
      },
    },
    plugins: {
      jest: eslintPluginJest,
    },
    rules: {
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
    },
  },
  {
    files: ['**/*.test.js', '**/__tests__/**/*.js'],
    plugins: {
      jest: eslintPluginJest,
    },
    rules: {
      ...eslintPluginJest.configs.all.rules,
    },
  },
];