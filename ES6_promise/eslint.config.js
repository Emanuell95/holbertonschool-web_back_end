import eslintComments from 'eslint-plugin-eslint-comments';

export default [
  {
    files: ['**/*.js'],
    plugins: {
      'eslint-comments': eslintComments
    },
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module'
    },
    rules: {
      'eol-last': ['error', 'always'],
      'eslint-comments/no-unused-disable': 'error'  // ejemplo de una regla útil del plugin
    }
  }
];
