import { useMemo } from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';
import Box from '@mui/material/Box';
import type { SxProps, Theme } from '@mui/material/styles';

interface Segment {
  kind: 'text' | 'inline' | 'display';
  value: string;
}

function split(src: string): Segment[] {
  const out: Segment[] = [];
  const re = /\$\$([\s\S]+?)\$\$|\$([^$]+?)\$/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = re.exec(src))) {
    if (m.index > last) out.push({ kind: 'text', value: src.slice(last, m.index) });
    if (m[1] !== undefined) out.push({ kind: 'display', value: m[1] });
    else out.push({ kind: 'inline', value: m[2] });
    last = re.lastIndex;
  }
  if (last < src.length) out.push({ kind: 'text', value: src.slice(last) });
  return out;
}

function render(tex: string, displayMode: boolean): string {
  return katex.renderToString(tex, { displayMode, throwOnError: false, strict: false });
}

interface Props {
  children: string;
  sx?: SxProps<Theme>;
  component?: React.ElementType;
}

export default function MathText({ children, sx, component = 'span' }: Props) {
  const segments = useMemo(() => split(children), [children]);
  return (
    <Box component={component} sx={{ lineHeight: 2, whiteSpace: 'pre-line', ...sx }}>
      {segments.map((s, i) => {
        if (s.kind === 'text')
          return (
            <span key={i}>
              {s.value.split(/\*\*(.+?)\*\*/g).map((part, j) => (j % 2 ? <strong key={j}>{part}</strong> : part))}
            </span>
          );
        if (s.kind === 'display')
          return (
            <span
              key={i}
              dir="ltr"
              style={{ display: 'block', overflowX: 'auto', overflowY: 'hidden', margin: '4px 0' }}
              dangerouslySetInnerHTML={{ __html: render(s.value, true) }}
            />
          );
        return (
          <span
            key={i}
            dir="ltr"
            style={{ unicodeBidi: 'isolate', display: 'inline-block' }}
            dangerouslySetInnerHTML={{ __html: render(s.value, false) }}
          />
        );
      })}
    </Box>
  );
}
