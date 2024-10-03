import type { RequestHandler } from '@sveltejs/kit';

export const GET: RequestHandler = async () => {
	const data = [
		{
			id: 1,
			name: 'John Doe',
			email: 'john.doe@example.com'
		},
		{
			id: 2,
			name: 'Jane Doe',
			email: 'jane.doe@esample.com'
		}
	];

	return new Response(JSON.stringify(data), { status: 200 });
};
