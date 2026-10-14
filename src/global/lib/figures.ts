/**
 * Question figures live next to their unit (src/semesters/<semester>/<unit>/fig/<id>.svg) and the
 * question data refers to them as "fig/<id>.svg". Vite bundles every such file; this maps the
 * file name to its built URL. Figure file names are question ids, so they are unique site-wide.
 */
const files = import.meta.glob<string>('../../semesters/**/fig/*.svg', { eager: true, query: '?url', import: 'default' });

const urlByName = new Map<string, string>();
for (const [path, url] of Object.entries(files)) {
  const name = path.slice(path.lastIndexOf('/') + 1);
  if (urlByName.has(name)) throw new Error(`duplicate figure ${name}`);
  urlByName.set(name, url);
}

export function figureUrl(figure: string): string {
  const url = urlByName.get(figure.slice(figure.lastIndexOf('/') + 1));
  if (!url) throw new Error(`missing figure ${figure}`);
  return url;
}
