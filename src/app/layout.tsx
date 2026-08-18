import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Vasuki Business Studio",
  description: "Create quotations, catalogs and manage clients from one beautiful workspace.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
