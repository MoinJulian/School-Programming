import { FlatCompat } from '@eslint/eslintrc';
import js from '@eslint/js';
import typescriptEslint from '@typescript-eslint/eslint-plugin';
import tsParser from '@typescript-eslint/parser';
import eslintComments from 'eslint-plugin-eslint-comments';
import globals from 'globals';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import parser from 'svelte-eslint-parser';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
	baseDirectory: __dirname,
	recommendedConfig: js.configs.recommended,
	allConfig: js.configs.all
});

export default [
	{
		ignores: [
			'**/.DS_Store',
			'**/node_modules',
			'build',
			'.svelte-kit',
			'package',
			'**/.env',
			'**/.env.*',
			'!**/.env.example',
			'**/pnpm-lock.yaml',
			'**/package-lock.json',
			'**/yarn.lock',
			'coverage',
			'__mocks__',
			'**/src/routes/api/utils/types/models.ts',
			'db',
			'docs/.astro/',
			'docs/dist/',
			'docs/src/env.d.ts'
		]
	},
	...compat.extends(
		'eslint:recommended',
		'plugin:@typescript-eslint/recommended',
		'plugin:svelte/recommended',
		'prettier'
	),
	{
		plugins: {
			'@typescript-eslint': typescriptEslint,
			'eslint-comments': eslintComments
		},

		languageOptions: {
			globals: {
				...globals.browser,
				...globals.node
			},

			parser: tsParser,
			ecmaVersion: 2020,
			sourceType: 'module',

			parserOptions: {
				extraFileExtensions: ['.svelte']
			}
		}
	},
	{
		files: ['**/*.svelte'],

		languageOptions: {
			parser: parser,
			ecmaVersion: 5,
			sourceType: 'script',

			parserOptions: {
				parser: '@typescript-eslint/parser'
			}
		}
	},
	{
		rules: {
			'@typescript-eslint/naming-convention': [
				'error',
				{
					selector: 'variable',
					format: ['snake_case'],
					leadingUnderscore: 'allow',
					filter: {
						regex: '^(__filename|__dirname|GET|POST)$', // Ignore specific cases
						match: false
					}
				},
				{
					selector: 'function',
					format: ['camelCase']
				},
				{
					selector: 'typeLike',
					format: ['PascalCase']
				},
				{
					selector: 'enumMember',
					format: ['UPPER_CASE']
				},
				{
					selector: 'interface',
					format: ['PascalCase']
				},
				{
					selector: 'parameter',
					format: ['camelCase', 'snake_case'],
					leadingUnderscore: 'allow'
				}
			],
			quotes: ['error', 'single'],
			'no-useless-escape': 'error',
			'@typescript-eslint/no-explicit-any': 'error',
			'eslint-comments/no-use': ['error', { allow: [] }]
		}
	}
];
