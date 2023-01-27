import { Head, Html, Main, NextScript } from 'next/document';

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <style>{`body { margin: 0 } *{
          transition: all 0.25s ease-in-out;
        }`}</style>
      </Head>
      <body
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          background: '#efefef',
        }}
      >
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
