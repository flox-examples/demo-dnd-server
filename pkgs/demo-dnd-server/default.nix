{
  self,
  python3Packages,
}:
python3Packages.buildPythonApplication {
  pname = "demo-dnd-server";
  version = "0.0.0";
  src = self;
  PIP_DISABLE_PIP_VERSION_CHECK = 1;
  meta.description = "A server that queries a D&D 5th Edition API";
  meta.maintainers = ["zmitchell"];
}
