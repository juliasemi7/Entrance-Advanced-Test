# ========== КОМАНДА /RESULTS ==========
@dp.message(Command("results"))
async def cmd_results(message: Message):
    user_id = message.from_user.id
    
    if user_id != TEACHER_ID:
        await message.answer("⛔ <b>Access denied.</b> This command is for teacher only.", parse_mode="HTML")
        return
    
    try:
        if os.path.exists('detailed_answers.json'):
            with open('detailed_answers.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if data:
                # Статистика
                stats_text = f"👩‍🏫 <b>TEACHER DASHBOARD</b>\n\n"
                stats_text += f"📊 <b>Всего тестов:</b> {len(data)}\n\n"
                stats_text += f"📋 <b>Все студенты:</b>\n"
                
                for i, test in enumerate(data, 1):
                    name = test.get('name', f'Student {i}')
                    score = test.get('score', 0)
                    max_score = test.get('max_score', sum(q['points'] for q in questions))
                    percentage = test.get('percentage', 0)
                    level = test.get('level', 'Unknown')
                    
                    stats_text += f"{i}. <b>{name}</b> - {score}/{max_score} ({percentage:.1f}%) - {level}\n"
                
                await message.answer(stats_text, parse_mode="HTML")
                
                # ИНЛАЙН-КНОПКИ ДЛЯ ВЫБОРА УЧЕНИКА
                builder = InlineKeyboardBuilder()
                
                for i, test in enumerate(data):
                    name = test.get('name', f'Student {i+1}')
                    score = test.get('score', 0)
                    max_score = test.get('max_score', sum(q['points'] for q in questions))
                    
                    button_text = f"{i+1}. {name} - {score}/{max_score}"
                    
                    if len(button_text) > 40:
                        short_name = name[:15] + "..." if len(name) > 15 else name
                        button_text = f"{i+1}. {short_name} - {score}/{max_score}"
                    
                    builder.add(InlineKeyboardButton(
                        text=button_text,
                        callback_data=f"view_details_{i}"
                    ))
                
                builder.adjust(1)
                
                await message.answer(
                    "📝 <b>Нажми на ученика для детального отчета:</b>",
                    parse_mode="HTML",
                    reply_markup=builder.as_markup()
                )
                
                # Отправляем CSV файл
                if os.path.exists('results.csv'):
                    csv_file = FSInputFile('results.csv')
                    await message.answer_document(csv_file, caption="📊 CSV файл со всеми результатами")
                
            else:
                await message.answer("📭 <b>Нет данных о тестах.</b>", parse_mode="HTML")
        else:
            # Если нет JSON, пробуем CSV
            if os.path.exists('results.csv'):
                with open('results.csv', 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    rows = list(reader)
                
                if len(rows) > 1:
                    total_tests = len(rows) - 1
                    stats_text = f"👩‍🏫 <b>TEACHER DASHBOARD</b>\n\n"
                    stats_text += f"📊 <b>Всего тестов:</b> {total_tests}\n\n"
                    
                    for i, row in enumerate(rows[1:], 1):
                        if len(row) >= 11:
                            name = row[3] if row[3] else f"Student {i}"
                            score = row[7] if len(row) > 7 else "0"
                            max_score = row[8] if len(row) > 8 else str(sum(q['points'] for q in questions))
                            percentage = row[9] if len(row) > 9 else "0%"
                            
                            stats_text += f"{i}. <b>{name}</b> - {score}/{max_score} ({percentage})\n"
                    
                    await message.answer(stats_text, parse_mode="HTML")
                    
                    csv_file = FSInputFile('results.csv')
                    await message.answer_document(csv_file, caption="📊 CSV файл со всеми результатами")
                else:
                    await message.answer("📭 <b>Нет результатов тестов.</b>", parse_mode="HTML")
            else:
                await message.answer("📭 <b>Нет результатов тестов.</b>", parse_mode="HTML")
            
    except Exception as e:
        await message.answer(f"❌ Ошибка: {str(e)}")
