// Build 1_claude_code_basic module deck (Fathom) via html2pptx from lecture/v1.1/_build/node_modules
const NM="/Users/samzheng/Documents/2_AI_Projects/0_AI+UX/AI_Agent/lecture/v1.1/_build/node_modules";
const path=require("path"), fs=require("fs");
const Module=require("module"); Module.globalPaths.push(NM); process.env.NODE_PATH=NM; Module._initPaths();
const pptxgen=require(path.join(NM,"pptxgenjs"));
const html2pptx=require("/Users/samzheng/.claude/commands/huashu-data-pro/scripts/html2pptx.js");
const HERE=__dirname, OUT=path.join(HERE,".."), VALIDATE=process.argv.includes("--validate");
(async()=>{
  const pptx=new pptxgen(); pptx.layout="LAYOUT_16x9";
  const dir=path.join(HERE,"html");
  const files=fs.readdirSync(dir).filter(f=>f.endsWith(".html")).sort();
  let err=0;
  for(const f of files){
    try{ await html2pptx(path.join(dir,f),pptx); if(!VALIDATE)process.stdout.write(`  ${f} ok\n`); }
    catch(e){ err++; console.log(`  [ERR] ${f}\n       ${e.message.replace(/\n/g,"\n       ")}`); }
  }
  if(!VALIDATE && err===0){ await pptx.writeFile({fileName:path.join(OUT,"1_claude_code_basic_数据叙事风.pptx")}); console.log("SAVED 1_claude_code_basic_数据叙事风.pptx"); }
  console.log(VALIDATE?`VALIDATE errors=${err}`:`BUILD errors=${err}`);
  if(err>0)process.exitCode=1;
})();
