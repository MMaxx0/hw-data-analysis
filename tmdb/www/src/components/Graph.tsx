import { useRef } from "react";
import { useGraph } from "@/hooks/useGraph";
import type { SigmaNodeEventPayload } from "sigma/types";

export function Graph({
  onNodeClick,
}: {
  onNodeClick?: (payload: SigmaNodeEventPayload) => void;
}) {
  const graphContainerRef = useRef<HTMLDivElement>(null);
  useGraph({
    containerRef: graphContainerRef,
    onNodeClick,
  });

  return <div id="graph" ref={graphContainerRef}></div>;
}
