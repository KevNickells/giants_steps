{
  description = "some auld cack";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};

      pythonEnv = pkgs.python312.withPackages (ps: with ps; [
          pyaudio
          numpy
	  portaudio
      ]);
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          pythonEnv
        ];
      };
    };
}
