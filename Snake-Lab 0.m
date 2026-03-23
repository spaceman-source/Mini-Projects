% 
function Snake_Game
    gridsize = 10;
    figure;
    axis([1 gridsize 1 gridsize]);
    hold on;
    title('The Snake Game');
    
    % Starting positions
    snake = [2, 5; 3, 5; 4, 5]; % Initial snake position
    apple = [5,8];
    
    
    apple = [randi(gridsize), randi(gridsize)]; % Initial apple position
    
    % Plot initial snake and apple
    snakePlot = plot(snake(:, 1), snake(:, 2), 'gs', 'MarkerFaceColor', 'g');
    applePlot = plot(apple(1), apple(2), 'rs', 'MarkerFaceColor', 'r');
    

    % Game loop
    while true
        % Get the current head of the snake
        head = snake(end, :);
        

        % Choose the direction to move
        direction = chooseDirection(head, apple, snake, gridsize);
        
        % Calculate the new head position
        newhead = head + direction;
        
        % Check for game over conditions
        if newhead(1) < 1 || newhead(1) > gridsize || newhead(2) < 1 || newhead(2) > gridsize
            msgbox('HIT THE WALL');
            break;
        end
        
        if ismember(newhead, snake, 'rows')
            msgbox('SELF DESTRUCTION');
            break;
        end
        
        % Makes snake grow when eats the apple
        if isequal(newhead, apple)
            % Grow the snake
            snake = [snake; newhead];
            % Generates another apple
            apple = [randi(gridsize), randi(gridsize)];
        else
            % Move the snake forward
            snake = [snake(2:end, :); newhead];
        end
        
        % Update plot
        set(snakePlot, 'XData', snake(:, 1), 'YData', snake(:, 2));
        set(applePlot, 'XData', apple(1), 'YData', apple(2));
        
        % Speed of snake
        pause(0.20);
    end
end


% How the snake moves
function direction = chooseDirection(head, apple, snake, gridsize)
    % Possible directions: right, left, up, down
    directions = [0, 1; 0, -1; -1, 0; 1, 0];
    
    bestDirection = [0, 0];
    minDistance = inf;
    
    % Where to go
    for i = 1:size(directions, 1)
        newHead = head + directions(i, :);
        


        % Make sure snake head is in boundaries also not hitting itself
        if newHead(1) >= 1 && newHead(1) <= gridsize && ...
           newHead(2) >= 1 && newHead(2) <= gridsize && ...
           ~ismember(newHead, snake, 'rows')
           
            % Calculate the distance to the apple
            distance = norm(newHead - apple);
            
            % Choose shortest distance
            if distance < minDistance
                minDistance = distance;
                bestDirection = directions(i, :);
            end
        end
    end
    
    direction = bestDirection;
end
