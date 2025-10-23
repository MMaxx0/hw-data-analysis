import { useState } from "react";
import { Graph } from "@/components/Graph";
import { ActorWidget } from "@/components/actorWidget";
import type { MovieCastMember } from "@/types/movies";

export default function App() {
  const [selectedActorNode, setSelectedActorNode] =
    useState<MovieCastMember | null>(null);

  return (
    <>
      <Graph
        onNodeClick={(payload) =>
          setSelectedActorNode(JSON.parse(payload.node))
        }
      />
      <div id="overlay" className="p-10 w-fit">
        <ActorWidget actorNode={selectedActorNode} />
      </div>
    </>
  );
}
