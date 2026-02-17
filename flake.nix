{
  description = "giant steps microtonal chords";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils  }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      pythonEnv = pkgs.python312.withPackages (ps: with ps; [
          pyaudio
          numpy
      ]);
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          pythonEnv
          pkgs.portaudio
          pkgs.nodejs_24
          pkgs.nodePackages.npm
        ];
        shellHook = ''
          echo "Node.js version: $(node --version)"
          echo "npm version: $(npm --version)"
          echo "Ready to develop! Try: npx serve ."
        '';
      };
    };
}
